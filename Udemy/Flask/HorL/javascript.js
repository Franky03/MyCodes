function pegarTexto() {
    const input= document.querySelector(".inp-name");
    console.log(input.value);
};

function getJson() {
    const number= document.querySelector(".inp-name").value;

    const dict_values= {number}
    const s = JSON.stringify(dict_values);
    console.log(s);
    window.alert(s)

    $.ajax({
        url:"/test",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
}