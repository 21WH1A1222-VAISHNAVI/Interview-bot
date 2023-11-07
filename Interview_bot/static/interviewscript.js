let currentQuestion = 0;
const questions = {{ questions | tojson | safe }};

function nextQuestion() {
    currentQuestion++;
    if (currentQuestion < questions.length) {
        document.getElementById('questionNumber').innerText = currentQuestion + 1;
        document.getElementById('questionText').innerText = questions[currentQuestion];
        document.getElementById('answer').value = '';
    } else {
        document.querySelector('section').innerHTML = "<h2>Interview Completed</h2><p>Thank you for answering the questions.</p>";
    }
}

// Immediately invoke the function to set up the initial question
(function () {
    document.getElementById('questionNumber').innerText = currentQuestion + 1;
})();
