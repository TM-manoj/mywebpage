<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Simple Web Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
      text-align: center;
      padding: 50px;
    }
    h1 {
      color: #333;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <h1>Welcome to My Simple Web Page</h1>
  <p>This is a paragraph of text.</p>
  <button onclick="sayHello()">Click Me!</button>

  <script>
    function sayHello() {
      alert("Hello there!");
    }
  </script>

</body>
</html>
