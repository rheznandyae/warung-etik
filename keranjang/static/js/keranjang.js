const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const keranjangList = document.querySelector(".list-keranjang")
const container = document.querySelector(".container-lg")
const username = JSON.parse(document.getElementById('username').textContent)

async function update_total_harga(){
    await fetch(`/keranjang/api/gettotalprice/${username}`,{
        method:'GET',
    })
    .then((res) => res.json())
    .then((item) => {
        if (document.contains(document.querySelector("#button-checkout"))) {
            document.querySelector("#button-checkout").remove();
        } 
        if (item.total_item > 0){
            container.innerHTML += `
            <a type="button" id="button-checkout" onclick="update_total_harga()" style="background-color: #38A169; color: #FFFFFF" class="btn col-7 col-md-5 mt-3 mb-3 mt-md-5 mb-md-5 fw-bold" href="/transaksi/">
                Checkout - ${item.total_price}
            </a> 
        `
        }
    })
}
async function getListItemKeranjang(){
    keranjangList.innerHTML = ''
    await fetch(`/keranjang/api/getbyusername/${username}/`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
            console.log(data.length)

            
            data.forEach((item) => {
                keranjangList.innerHTML += `
                <div class="card item-${item.id} shadow col-12 col-sm-10 mt-2" style="max-width: 60rem;">
                    <div class="m-2 p-2">
                        <div class="row justify-content-center w-auto">
                            <div class="col-12 col-md-4 d-flex align-items-center justify-content-center">
                                <img class="rounded-3 img-fluid" src="${item.barang.image_url}" alt="">
                            </div> 
                            <div class="ms-2 card-body d-flex flex-column justify-content-between col-12 col-md-5 ">
                                <div>
                                    <h3><b>${item.barang.nama}</b></h3>
                                    <div style="
                                        position: relative;
                                        max-height:150px;
                                        overflow: auto;
                                        display: block;"
                                        class="mb-1 mb-md-3"
                                    >
                                        <p>
                                            ${item.barang.deskripsi}
                                        </p>
                                    </div>
                                    
                                </div>
                                <div>
                                    <h4 class="mb-3 "><b>Rp${item.barang.harga}</b></h4>
                                    <div>
                                        <div class="btn-group btn-quantity" role="group" aria-label="Basic mixed styles example">
                                            <button id="minus1-${item.id}" onClick="minus1_item_keranjang(${item.id})"  type="button" class="btn btn-danger"><b>-</b></button>
                                            <button id="banyak-item-${item.id}"type="button" class="" style="border: 0; cursor: default; width: 3rem;"><b>${item.jumlah_item}</b></button>
                                            <button id="plus1-${item.id}" onClick="plus1_item_keranjang(${item.id})" type="button" class="btn btn-success"><b>+</b></button>
                                        </div>
                                        <button id="hapus-item-${item.id}" onClick="hapus_item_keranjang(${item.id})" type="button" class="btn ms-1">🗑️</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                `
            });
        })
    update_total_harga()
        

    
}

async function plus1_item_keranjang(id){
    const data = new FormData()
    data.append('id_keranjang', id)
    data.append('csrfmiddlewaretoken', csrftoken )
    await fetch(`/keranjang/api/plus1/`,{
        method:'POST',
        body:data
    })
    .then((res) => res.json())
    .then((item) => {
        console.log(item.id)
        const itemKeranjangUpdated = document.querySelector(`#banyak-item-${item.id}`)
        itemKeranjangUpdated.innerHTML = `
            <b>${item.jumlah_item}</b>
        `
    })
    update_total_harga()
}

async function minus1_item_keranjang(id){
    const data = new FormData()
    data.append('id_keranjang', id)
    data.append('csrfmiddlewaretoken', csrftoken )
    await fetch(`/keranjang/api/minus1/`,{
        method:'POST',
        body:data
    })
    .then((res) => res.json())
    .then((item) => {
        console.log(item.id)
        const itemKeranjangUpdated = document.querySelector(`#banyak-item-${item.id}`)
        itemKeranjangUpdated.innerHTML = `
            <b>${item.jumlah_item}</b>
        `
        if(item.jumlah_item === 0){
            document.querySelector(`.item-${item.id}`).remove()
        }
    })
    
    update_total_harga()
}

async function hapus_item_keranjang(id){
    const data = new FormData()
    data.append('id_keranjang', id)
    data.append('X-CSRFToken', csrftoken )
    await fetch(`/keranjang/api/${id}`,{
        method:'DELETE',
        body:data
    })
    .then((res) => res.json())
    .then((item) => {
    
        console.log(item)
        const itemKeranjangDeleted = document.querySelector(`.item-${id}`)
        itemKeranjangDeleted.remove()
    })

    update_total_harga()

}




getListItemKeranjang()