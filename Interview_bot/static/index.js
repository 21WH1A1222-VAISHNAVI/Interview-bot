function submitForm() {
  var name = document.getElementById('name').value;
  var university = document.getElementById('university').value;
  var major = document.getElementById('major').value;
  var email = document.getElementById('email').value;

  var messageContainer = document.getElementById('message');

  if (name && university && major && email) {
      var message = 'Form submitted successfully! Thank you, ' + name + '!';
      messageContainer.textContent = message;
  } else {
      messageContainer.textContent = 'Please fill in all fields.';
  }
}
