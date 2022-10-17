// index.js

// var number = 5; //one way to define variable
// let name = "Anjana";   // another way to define variable


// number = 12; // here i am updating the value of the variable 'number' 
// name = "Sumit" // here i am updating the name of the variable 'name'

// Writing to the document
// document.writeln(name + number);
// alert("Hello World");  // when this line executes alert as pop up come to the screen 

const formInfo = document.getElementById("formInfo");

let hasJob = false;
if (hasJob) {
// I have a job
    showMessage("Thanks for visiting, I am currently employed");
} else {
    showMessage("Please look around, I am currently looking for a position");
}

let today = new Date();
let DayOfWeek = today.getDay();
if (DayOfWeek === 0 || DayOfWeek === 6) {
    showMessage("Since it is weekend, please be patient with my returning your email :)");
}

function showMessage(message) {
 
    formInfo.innerHTML = "<p>" + message + "</p>";
}

function clearMessage() {
    formInfo.innerHTML = "";
}

const contactForm = document.getElementById("contactForm");
contactForm.addEventListener("submit", function (event) {
    event.preventDefault();
    showMessage("Sending your Message");
});

const Objectives = document.getElementsByClassName("Objective");
for (let x = 0; x < Objectives.length; x++) {
    const item = Objectives[x];
    item.addEventListener("mouseenter", function (event) {
        event.target.style = "background-color: lightgray;";
    });
    item.addEventListener("mouseleave", function (event) {
        event.target.style = "";    
});
}