### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome to My AWS Website</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Hello from AWS S3!</h1>
    <p>This website is hosted on Amazon S3, delivered via CloudFront, and secured with HTTPS!</p>
  </div>
</body>
</html>
```

---

### `style.css`

```css
body {
  margin: 0;
  font-family: sans-serif;
  background: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0,0,0,0.1);
  text-align: center;
}
```
