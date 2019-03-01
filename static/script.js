function count() {
  alert("Let's play a game: Who can count the highest?");
  var high = prompt("You start: how high can you count?");
  alert(high + "? I can count MUCH higher than that");
  alert("Prepare to be epic destroyed, human >:)");
  for (var i = 1; i <= parseInt(high) + 1; i++) {
    alert(i);
  }
  alert("#destroyed");
}

function destroy() {
  $("body").addClass("animated hinge");
  $("body").after('<p>Wanna reverse time? Press ctrl+r or cmd+r</p>');
}

function login() {
  $("#signup").html('<div id="login"><h2>Login</h2><form action="/login" method="POST"><label for="username">Username: </label><input type="text" name="username" id="username"><br><label for="hobby">Password: </label><input type="password" name="password" id="password"><br><input type="submit" value="Submit"></form><p>Need an account? <button onclick="signup();">Signup</button></p></div>');
}
function signup() {
  $("#login").html('<div id="signup"><h2>Signup</h2><form action="/signup" method="POST"><label for="username">Username: </label><input type="text" name="username" id="username"><br><label for="hobby">Password: </label><input type="password" name="password" id="password"><br><input type="submit" value="Submit"></form><p>Have an account? <button onclick="login();">Login</button></p></div>');
}
