<doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>lab_3</title>
</head>
<body>
    <h1>The Bulletin Board</h1>

    <form action="save.php" method="post">
        <label for="email">Email</label>
        <input type="email" name="email" required>

        <label for="title">Title</label>
        <input type="text" name="title" required><br>

        <label for="categories">Categories</label>
        <select name="categories" required>
            <option value="clothes">Clothes</option>
            <option value="electronics">Electronics</option>
            <option value="services">Services</option>
        </select>
    </form>

    <label for="description">Description:</label><br>
    <textarea name="text" rows="10" cols="54" required></textarea><br>

    <button type="submit">Post</button>

    <div id="form"…>
    <div id="table">
        <table>
            <thead>
                <th>Email</th>
                <th>Title</th>
                <th>Category</th>
                <th>Description</th>
            </thead>
            <tbody>
                <tr>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
