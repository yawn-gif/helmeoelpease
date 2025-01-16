{\rtf1\ansi\ansicpg1252\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 const gameText = document.getElementById('game-text');\
const playerInput = document.getElementById('player-input');\
const submitButton = document.getElementById('submit-button');\
const visual = document.getElementById('visual');\
\
// Define game scenes\
const scenes = \{\
  start: \{\
    text: "You're standing in a dark forest. Shadows move around you.",\
    visual: "forest.jpg",\
    next: \{\
      explore: "cabin",\
      run: "end"\
    \}\
  \},\
  cabin: \{\
    text: "You see a cabin with a flickering light inside. Enter?",\
    visual: "cabin.jpg",\
    next: \{\
      yes: "inside",\
      no: "end"\
    \}\
  \},\
  inside: \{\
    text: "Inside, you find a strange book glowing on the table.",\
    visual: "book.jpg",\
    next: \{\
      read: "curse",\
      ignore: "end"\
    \}\
  \},\
  curse: \{\
    text: "The book curses you. You are now a part of the forest.",\
    visual: "curse.jpg"\
  \},\
  end: \{\
    text: "You run, but the shadows catch you. The end.",\
    visual: "end.jpg"\
  \}\
\};\
\
// Track the current scene\
let currentScene = 'start';\
\
// Update the scene\
function updateScene() \{\
  const scene = scenes[currentScene];\
  gameText.innerText = scene.text;\
  visual.src = scene.visual;\
  playerInput.value = '';\
\}\
\
// Handle user input\
submitButton.addEventListener('click', () => \{\
  const input = playerInput.value.toLowerCase();\
  const scene = scenes[currentScene];\
\
  if (scene.next && scene.next[input]) \{\
    currentScene = scene.next[input];\
    updateScene();\
  \} else \{\
    gameText.innerText = "Invalid choice. Try again.";\
  \}\
\});\
\
// Initialize the game\
updateScene();\
}