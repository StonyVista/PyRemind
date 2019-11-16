// Get and Set JSON of Reminders
// Somehow output your Python to here ? 
// Ref ( https://stackoverflow.com/questions/32284317/send-python-information-to-a-javascript-file ) 

// Reminders JSON
var Reminders = {
	"reminders": [
		{
			"title" : "First Reminder",
			"body" : "A Reminder",
			"time" : "12:30",
		},
		{
			"title" : "Second Reminder",
			"body" : "A Reminder",
			"time" : "12:45",
		},
		{
			"title" : "First Reminder",
			"body" : "A Reminder",
			"time" : "12:30",
		},
		{
			"title" : "Second Reminder",
			"body" : "A Reminder",
			"time" : "12:45",
		},
		{
			"title" : "First Reminder",
			"body" : "A Reminder",
			"time" : "12:30",
		},
		{
			"title" : "Second Reminder",
			"body" : "A Reminder",
			"time" : "12:45",
		},
		{
			"title" : "First Reminder",
			"body" : "A Reminder",
			"time" : "12:30",
		},
		{
			"title" : "Second Reminder",
			"body" : "A Reminder",
			"time" : "12:45",
		}
	]
};

// Get Element for Outputting
var MainElement = document.getElementById("ShowRemindersArea");

// Declare Output String
var OutputString = "";

// For each JSON Reminder
for(var x = 0; x < Reminders["reminders"].length; x++) {
	// Add Container Start to Output String
	OutputString += "<div class='container bg-white shadow-lg rounded-lg my-6'>"
	
	// Add Title to Output String
	OutputString += "<h2 class='text-blue-400'>" + Reminders["reminders"][x]["title"] + "</h2>";
	
	// Add Body to Output String
	OutputString += "<div class='text-blue-200'>" + Reminders["reminders"][x]["body"] + "</div>";
	
	// Add Time to Output String
	OutputString += "<h3 class='text-blue-300'>" + Reminders["reminders"][x]["time"] + "</h3>";
	
	// Add Container End to Output String
	OutputString += "</div>";
}

// Output to Element
MainElement.innerHTML = OutputString;

// Get Element for Show Text for Button
var ShowReminders = document.getElementById("RemindersTextShow");

// Get Element for Hide Text for Button
var HideReminders = document.getElementById("RemindersTextHide");


// Function that uses these vars
function SwitchClassesAround(){
	MainElement.classList.toggle('hidden'); 
	ShowReminders.classList.toggle('hidden');  
	HideReminders.classList.toggle('hidden');
}