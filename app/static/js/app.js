window.onload = function() {
    // Get the microphone element
    const microphone = document.getElementById('microphone');
  
    // Get the response element
    const responseElement = document.getElementById('response');
  
    // Get the text element
    const textElement = document.getElementById('text');
  
    // Update the response and text elements with initial values
    responseElement.textContent = 'Response: ';
    textElement.textContent = 'You said: ';
  
    // Add click event listener to the microphone
    microphone.addEventListener('click', function() {
      // Update the response and text elements while listening
      responseElement.textContent = 'Response: Listening...';
      textElement.textContent = 'You said: Listening...';
  
      // Make an AJAX request to the '/process_microphone' route
      fetch('/process_microphone', {
        method: 'POST'
      })
        .then(response => response.text())
        .then(reply => {
          console.log('Response:', reply);
          // Update the response element with the generated reply
          responseElement.textContent = 'Response: ' + reply;
          // Update the text element with the recorded speech
          textElement.textContent = 'You said: ' + '{{ text }}';
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });
  };
  