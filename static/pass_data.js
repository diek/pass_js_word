// a function to take in the list of data, created in app.py
// add option items to the dom using the values.
function displayData(wings) {
  var selectWings = document.getElementById('chickenWings')
  var fragment = document.createDocumentFragment()
  for (i = 0; i < wings.length; i++){
    var option = document.createElement("option");
    option.text = wings[i];
    fragment.appendChild(option);
  }
  selectWings.appendChild(fragment);
}
