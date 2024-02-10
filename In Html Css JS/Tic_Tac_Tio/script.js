var btns = document.querySelectorAll(".btn");
var reset = document.querySelector("#reset button");
var X = true;
var winningpoint = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 4, 6],
    [2, 5, 8],
    [3, 4, 5],
    [6, 7, 8]
];
function checkwinner() {
    let boxtext = Array.from(btns).map(btn => btn.innerText);
    let winner = winningpoint.some(condition => {
        return condition.every(index => boxtext[index] === "X");
    })
    if (winner) {
        setTimeout(() => {
            alert("Player X was win");
            btns.forEach(btns => {
                btns.innerHTML = "";
            });
        }, 150);
    };
    winner = winningpoint.some(condition => {
        return condition.every(index => boxtext[index] === "O");
    })
    if (winner) {
        setTimeout(() => {
            alert("Player O was win");
            btns.forEach(btns => {
                btns.innerHTML = "";
            });
        }, 150);
    };
}
btns.forEach(btn => {
    btn.onclick = () => {
        if (btn.innerHTML != "") {
            return;
        }
        else if (X) {
            btn.innerHTML = "X";
            X = false;
        }
        else {
            btn.innerHTML = "O";
            X = true;
        }
        checkwinner();
    };

});
reset.onclick = () => {
    btns.forEach(btns => {
        btns.innerHTML = "";
    });
};