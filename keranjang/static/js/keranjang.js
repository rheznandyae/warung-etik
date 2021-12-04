const keranjangList = document.querySelector(".list-keranjang")
const loginId = JSON.parse(document.getElementById('user_id').textContent)

async function getListItemKeranjang(){
    keranjangList.innerHTML = ''
    fetch(`/keranjang/api/getbyusername/bobi/`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
            data.forEach((item) => {
                keranjangList.innerHTML += `
                <div class="card shadow col-12 col-md-8 mt-2">
                    <div class="m-2 p-2">
                        <div class="row justify-content-center w-auto">
                            <img class="rounded-3 img-fluid col-12 col-lg-4" src="${item.barang.image_url}" alt="">
                            <div class="ms-2 card-body d-flex flex-column justify-content-between col-12 col-lg-5 ">
                                <div>
                                    <h3><b>${item.barang.nama}</b></h3>
                                    <p>
                                        ${item.barang.deskripsi}
                                    </p>
                                </div>
                                <div>
                                    <h4 class="mb-3"><b>Rp${item.barang.harga}</b></h4>
                                    <div>
                                        <div class="btn-group btn-quantity" role="group" aria-label="Basic mixed styles example">
                                            <button id="minus1-${item.id}" type="button" class="btn btn-danger"><b>-</b></button>
                                            <button id="banyak-item-${item.id}"type="button" class="" style="border: 0; cursor: default; width: 3rem;"><b>${item.jumlah_item}</b></button>
                                            <button id="plus1-${item.id}" type="button" class="btn btn-success"><b>+</b></button>
                                        </div>
                                        <button id="hapus-item-${item.id}" type="button" class="btn ms-1">🗑️</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                `
            });
        })
}

getListItemKeranjang()