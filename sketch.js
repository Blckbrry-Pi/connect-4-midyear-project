function deepCopy(objectIn) {
    return JSON.parse(JSON.stringify(objectIn))
}
function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}


const newBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
];
function getBoardDimensions(){
    return width * 6/8 < height * 7/8 ? createVector(width  * 7  /  8, width  * 6  /  8) : createVector(height * 49 / 48, height * 7  /  8);
}
function getBoardPosition(boardDimensionVect){
    return createVector((width - boardDimensionVect.x) / 2, (height - boardDimensionVect.y) / 2) 
}

let currentBoard;




function setup() {
    createCanvas(windowWidth, windowHeight);

    currentBoard = deepCopy(newBoard);
}

function draw() {
    background(255);


    boardDimensionVector = getBoardDimensions();
    boardPosition = getBoardPosition(boardDimensionVector)

    push();
        translate(boardPosition.x, boardPosition.y);
        scale(boardDimensionVector.x / 700);
            drawBoard();
    pop();
}

function drawBoard(){
    rect(0, 0, 700, 600);
}