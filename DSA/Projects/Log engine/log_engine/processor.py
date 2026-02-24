    # Processor = metrics engine

from collections import deque
import heapq
from config import WINDOW_SECONDS, ERROR_THRESHOLD, IP_THRESHOLD


class LogProcessor:
    def __init__(self):
        self.logs = deque()
        self.error_count = 0
        self.service_counts = {}
        self.ip_counts = {}
        
        self.alerts = []    #alert storage

    def process(self, log):
        now = log["timestamp"]
        self.logs.append(log)

        # Update error count
        if log["level"] == "ERROR":
            self.error_count += 1

        # Update service count
        service = log["service"]
        self.service_counts[service] = self.service_counts.get(service, 0) + 1

        self.evict_old_logs(now)
        
        # Update IP counts        
        ip = log["ip"]
        self.ip_counts[ip] = self.ip_counts.get(ip, 0) + 1
        
        

    def evict_old_logs(self, current_time):
        while self.logs and (current_time - self.logs[0]["timestamp"]).total_seconds() > WINDOW_SECONDS:
            old_log = self.logs.popleft()

            # Decrement error count
            if old_log["level"] == "ERROR":
                self.error_count -= 1

            # Decrement service count
            service = old_log["service"]
            self.service_counts[service] -= 1
            if self.service_counts[service] == 0:
                del self.service_counts[service]

            # Decrement IP count                
            ip = old_log["ip"]
            self.ip_counts[ip] -= 1
            if self.ip_counts[ip] == 0:
                del self.ip_counts[ip]

    def get_error_rate(self):
        total = len(self.logs)
        if total == 0:
            return 0
        return self.error_count / total

    def get_service_counts(self):
        return self.service_counts
    

    def get_top_k_ips(self, k=3):
        if not self.ip_counts:
            return []
    
        # build min heap of size k
        heap = []
    
        for ip, count in self.ip_counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, ip))
            else:
                if count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, ip))
    
        # return sorted descending
        return sorted(heap, reverse=True)
    
    
    # alert logic
    def check_alerts(self):
        self.alerts.clear()
    
        # Error rate alert
        if self.get_error_rate() > 0.20:
            self.alerts.append("High error rate detected")
    
        # Suspicious IP alert
        for ip, count in self.ip_counts.items():
            if count > 50:  # threshold for demo
                self.alerts.append(f"High traffic from IP {ip}")
    
        return self.alerts