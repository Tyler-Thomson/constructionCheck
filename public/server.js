let express = require('express');
let bp = require('body-parser');
let app = express();
app.use(express.static(__dirname + '/client/static'));
app.use(bp.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', __dirname + '/client/views');
app.listen(8000, function () {
  console.log('listening on port 8000');
});
