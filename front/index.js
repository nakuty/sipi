addColumn = () => {
    let table_content = document.querySelectorAll(".gm-input > tbody > tr");
    table_content.forEach(tr => {
        let td = document.createElement("td");
        td.addEventListener('dblclick', dbClickListener);
        tr.querySelector(":last-child").before(td);
    });

    document.querySelector(".gm-input-2head").colSpan += 1;
}

addRow = () => {
    let row_length = document.querySelector(".gm-input > tbody > tr").querySelectorAll("td").length;

    let new_row = document.createElement("tr");
    for(let i = 0; i < row_length;i++){
        let td = document.createElement("td");
        td.addEventListener('dblclick', dbClickListener);
        new_row.appendChild(td);
    }

    document.querySelector(".gm-input > tbody > tr:last-child").before(new_row)
}

function dbClickListener() {
    let input = document.createElement('input');
    input.value = this.innerHTML;
    this.innerHTML = '';
    input.style.width = 24 + "px";
    this.appendChild(input);
    input.focus()

    let td = this;
    input.addEventListener('blur', function() {
        td.innerHTML = this.value;
        td.addEventListener('dblclick', dbClickListener);
    });

    this.removeEventListener('dblclick', dbClickListener);
}

async function calculate(){
    let sysEq = []
    let func = ""
    let trs = document.querySelectorAll("tbody tr")

    for(let i = 0; i < trs.length; i++){
        let tds = trs[i].querySelectorAll("td")
        let eq = ""
        if (i !== (trs.length - 1)){
            for(let j = 0; j < tds.length; j++){
                if (j === 0) continue;
                eq += tds[j].innerText
                if(j !== tds.length - 1) eq += ` * x${j}`
                if(j < tds.length - 2)eq += " + "
                if(j === tds.length - 2) eq += " <= "

                if(tds[j].innerText === "") console.log("Введены не все параметры")
            }
            sysEq.push(eq)
        }
        else{
            for(let j = 0; j < tds.length; j++){
                if(j === 0 || j === tds.length -1) continue;
                func += tds[j].innerText + ` * x${j} `
                if(j !== tds.length - 2) func += "+ "
            }
        }
    }

    document.querySelector(".output").innerText = await eel.mid_simplex(func, "max", sysEq.length, sysEq)();

}

function changeCSS(cssFile, cssLinkIndex) {

    var oldlink = document.getElementsByTagName("link").item(cssLinkIndex);

    var newlink = document.createElement("link");
    newlink.setAttribute("rel", "stylesheet");
    newlink.setAttribute("type", "text/css");
    newlink.setAttribute("href", cssFile);

    document.getElementsByTagName("head").item(cssLinkIndex).replaceChild(newlink, oldlink);
}

(() => {
    var tds = document.querySelectorAll('td');

for (var i = 0; i < tds.length; i++) {
	tds[i].addEventListener('dblclick', dbClickListener);
}
})()