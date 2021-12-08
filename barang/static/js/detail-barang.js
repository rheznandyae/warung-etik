    let data = 1;
    
    
    data = document.getElementById("counting").innerText;
    temp = document.getElementById("valueCount");
    console.log(temp.value);


    
    function increment() {
        if(data == 1){
            data = 2;
        }
        else {
            data = data + 1;
        }
        document.getElementById("counting").innerText = data;
        document.getElementById("valueCount").value = data;
    }

    function decrement() {
        if(data>1) {
            data = data - 1;
            valueCount = valueCount - 1;
        }
        document.getElementById("counting").innerText = data;
        document.getElementById("valueCount").value = data;
    }
