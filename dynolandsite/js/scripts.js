$.get("../score.json", function(data){
    var string1 = JSON.stringify(data);
    let responseJson = JSON.parse(string1);
    var nbscore = 0;

    Object.keys(responseJson['score']).forEach((tab)=>{
        nbscore++;
    })
    var tab = new Array(nbscore);
    var i = 0;
    for(var key in data['score']) {
        tab[i] = [];
        tab[i][0] =key;
        tab[i][1] = data['score'][key];
        i++;
    }

    var nompremier = "";
    var scorepremier = 0;

    var nomdeuxieme = "";
    var scoredeuxieme = 0;

    var nomtroisieme = "";
    var scoretroisieme = 0;


    tab.forEach((tab) => {

        if(tab[1] > scorepremier){
            nomdeuxieme = nompremier;
            scoredeuxieme = scorepremier;

            nompremier = tab[0];
            scorepremier = tab[1];

        }else if(tab[1] > scoredeuxieme){
            nomtroisieme = nomdeuxieme;
            scoretroisieme = scoredeuxieme;

            nomdeuxieme = tab[0];
            scoredeuxieme = tab[1];
        }else if(tab[1] > scoretroisieme){
            nomtroisieme = tab[0];
            scoretroisieme = tab[1];
        }else{

        }

    })

    document.getElementById("premier").innerHTML += "<td>"+nompremier+"</td> <td>"+scorepremier+"</td>";
    document.getElementById("deuxieme").innerHTML += "<td>"+nomdeuxieme+"</td><td> "+scoredeuxieme+"</td>";
    document.getElementById("troisieme").innerHTML += "<td>"+nomtroisieme+"</td><td> "+scoretroisieme+"</td>";
});