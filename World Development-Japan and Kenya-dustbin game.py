import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Geography Game", layout="wide")
st.title("World Development: Japan and Kenya")
st.write("Drag the fact card from the middle and drop it into the correct bin!")

drag_and_drop_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    text-align: center;
    color: #333;
    /* Streamlit's default background color */
    background-color: transparent; 
  }
  .score-board {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #ff4b4b;
  }
  .fact-container {
    height: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 40px;
  }
  .fact-card {
    background: #ffffff;
    border: 3px solid #0068c9;
    padding: 20px 40px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: bold;
    cursor: grab;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    user-select: none;
    transition: transform 0.2s;
  }
  .fact-card:active {
    cursor: grabbing;
    transform: scale(0.95);
  }
  .bins-container {
    display: flex;
    justify-content: space-around;
    gap: 15px;
    padding: 10px;
  }
  .bin {
    flex: 1;
    height: 200px;
    background: #f8f9fb;
    border: 3px dashed #a0aab5;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: bold;
    transition: all 0.3s ease;
  }
  .bin.drag-over {
    background: #e6f3ff;
    border-color: #0068c9;
    transform: scale(1.05); /* Makes the box pop out when hovering */
  }
  .bin img {
    width: 70px;
    margin-bottom: 15px;
  }
</style>
</head>
<body>

  <div class="score-board">Score: <span id="score">0</span></div>

  <!-- The Draggable Card -->
  <div class="fact-container">
    <div id="fact-card" class="fact-card" draggable="true">Loading...</div>
  </div>

  <!-- The Four Drop Zones -->
  <div class="bins-container">
    <div class="bin" id="Japan Facts">
      <img src="https://cdn-icons-png.flaticon.com/128/197/197604.png" alt="Japan">
      Japan Facts
    </div>
    <div class="bin" id="Kenya Facts">
      <img src="https://cdn-icons-png.flaticon.com/128/197/197608.png" alt="Kenya">
      Kenya Facts
    </div>
    <div class="bin" id="Japan Reasons">
      <img src="https://cdn-icons-png.flaticon.com/128/3079/3079165.png" alt="Japan Gear">
      Japan Reasons
    </div>
    <div class="bin" id="Kenya Reasons">
      <img src="https://cdn-icons-png.flaticon.com/128/3079/3079165.png" alt="Kenya Gear">
      Kenya Reasons
    </div>
  </div>

  <script>
    // 1. Game Data
    const facts = [
      {"text": "33,600 GDP per person", "cat": "Japan Facts"},
      {"text": "4th wealthiest country", "cat": "Japan Facts"},
      {"text": "HDI of 0.953", "cat": "Japan Facts"},
      {"text": "Life expectancy: 83", "cat": "Japan Facts"},
      {"text": "1240 GDP per person", "cat": "Kenya Facts"},
      {"text": "Infant mortality: 58", "cat": "Kenya Facts"},
      {"text": "HDI of 0.521", "cat": "Kenya Facts"},
      {"text": "Life expectancy: 57", "cat": "Kenya Facts"},
      {"text": "Rapid industrialisation", "cat": "Japan Reasons"},
      {"text": "Trade surplus", "cat": "Japan Reasons"},
      {"text": "Secondary and tertiary industries", "cat": "Japan Reasons"},
      {"text": "Long working hours", "cat": "Japan Reasons"},
      {"text": "Mostly primary sector industries", "cat": "Kenya Reasons"},
      {"text": "Previous colony", "cat": "Kenya Reasons"},
      {"text": "Large trade deficit", "cat": "Kenya Reasons"},
      {"text": "Mostly growing cash crop", "cat": "Kenya Reasons"}
    ];

    let currentFact = null;
    let score = 0;

    const factCard = document.getElementById('fact-card');
    const scoreElement = document.getElementById('score');
    const bins = document.querySelectorAll('.bin');

    // 2. Pick a random fact
    function loadNewFact() {
      const randomIndex = Math.floor(Math.random() * facts.length);
      currentFact = facts[randomIndex];
      factCard.innerText = currentFact.text;
    }

    // 3. Set up the "Drag"
    factCard.addEventListener('dragstart', (e) => {
      // Secretly store the correct category inside the dragged item
      e.dataTransfer.setData('text/plain', currentFact.cat);
      setTimeout(() => { factCard.style.opacity = '0.4'; }, 0);
    });

    factCard.addEventListener('dragend', (e) => {
      factCard.style.opacity = '1'; // Reset opacity when dropped
    });

    // 4. Set up the "Drop Zones" (The 4 Boxes)
    bins.forEach(bin => {
      // Allow dropping
      bin.addEventListener('dragover', (e) => {
        e.preventDefault(); 
        bin.classList.add('drag-over');
      });

      // Remove the highlight if we drag away
      bin.addEventListener('dragleave', (e) => {
        bin.classList.remove('drag-over');
      });

      // Handle the actual drop
      bin.addEventListener('drop', (e) => {
        e.preventDefault();
        bin.classList.remove('drag-over');
        
        // Retrieve the secret category we stored during dragstart
        const correctCategory = e.dataTransfer.getData('text/plain');
        
        // Check if the Box ID matches the correct category
        if (bin.id === correctCategory) {
          score++;
          scoreElement.innerText = score;
          // Flash green for correct
          bin.style.backgroundColor = '#d4edda';
          bin.style.borderColor = '#28a745';
        } else {
          // Flash red for incorrect
          bin.style.backgroundColor = '#f8d7da';
          bin.style.borderColor = '#dc3545';
        }
        
        // Return to normal color after a half-second
        setTimeout(() => { 
            bin.style.backgroundColor = '#f8f9fb'; 
            bin.style.borderColor = '#a0aab5';
        }, 500);
        
        // Load the next question immediately!
        loadNewFact();
      });
    });

    // Start the game!
    loadNewFact();
  </script>
</body>
</html>
"""

st.iframe(drag_and_drop_html, height=600)