window.onload = function(){

    var stage = document.getElementById('stage');
    var context = stage.getContext("2d");
    
    setInterval(game, 100);

    const vel = 1; 
    var velX = 0;
    var velY = 0;
    var positionX = 10;
    var positionY = 15;
    var lenPeca = 20;
    var quantPeca = 20;
    var ax = 15;
    var ay = 15;

    var trail = []
    tail = 5; 

    function game(){
        positionX += velX;
        positionY += velY;
        // Se a snake estiver vindo para esquerda e chega o limite, menor
        //  que zero, faz atravessar o outro lado (quantPeca - 1) = 19
        if(positionX < 0){    
            positionX = quantPeca - 1;
        }

        // Se a snake estiver vindo para direira e chega o limite, maior
        //  que quantidade de peças, faz atravessar o outro lado, zero
        if(positionX > quantPeca - 1){
            positionX = 0;
        }
        
        // Se a snake estiver vindo para cima e chega o limite, menor
        //  que zero, faz atravessar de baixo (quantPeca - 1) = 19
        if(positionY < 0){
            positionY = quantPeca - 1;
        }
        
        // Se a snake estiver vindo para baixo e chega o limite, maior
        //  que quantidade de peças, faz atravessar de cima, zero
        if(positionY > quantPeca - 1){
            positionY = 0;
        }

        // cor do fundo
        context.fillStyle = "black";
        context.fillRect(0,0, stage.width, stage.height);

        // cor da Maçã 
        context.fillStyle = "red"
        // .fillReact(ax*lenPeca, ay*lenPeca, lenPeca, lenPeca)
        context.fillRect(ax*lenPeca, ay*lenPeca, lenPeca,lenPeca)
        
        // cor da snake
        context.fillStyle = "gray";

        // for(var i = 0; i < trail.length; i++){
        //     context.fillReact(trail[i].x*lenPeca, trail[i].y*lenPeca, lenPeca-1, lenPeca-1)
        //     if(trail[i].x == positionX && trail[i].y == positionY){
        //         velX = 0;
        //         velY = 0;
        //         tail = 5
        //     }
        // }


        for (var i = 0; i < trail.length; i++) {
            context.fillRect(trail[i].x*lenPeca, trail[i].y*lenPeca, lenPeca-1, lenPeca-1);
            if (trail[i].x == positionX && trail[i].y == positionY)
            {
                velX = velY=0;
                tail = 5;
            }
        }

        // retira o proximo valor correspondente a cabeça do rastro da snake para evitar o rastro seja maior que a causa
        trail.push({x:positionX, y:positionY})
        while(trail.length > tail){
            trail.shift();
        }

        // aumentar o tamanho da snake cada vez que ela comer a maça criar maças aleatoriamente 
        if(ax==positionX && ay==positionY){
            tail++;
            ax = Math.floor(Math.random()*quantPeca);
            ay = Math.floor(Math.random()*quantPeca);
        }

    // função para controlar a cobrar 
    document.addEventListener('keydown', keyPush);
    function keyPush(event){
        switch (event.keyCode) {
            case 37: // Left
                velX = -vel;
                velY = 0;
                break;
            case 38: // up
                velX = 0;
                velY = -vel;
                break;
            case 39: // right
                velX = vel;
                velY = 0;
                break;
            case 40: // down
                velX = 0;
                velY = vel;
                break;          
            default:
                    
                break;
        }
    }
}
}