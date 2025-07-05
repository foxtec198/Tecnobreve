// exampleModal
var spinner = '<span id="spin_ldg" class="spinner-border spinner-border-sm text-light" role="status"></span>'
const email = 'foxtec198@gmail.com' 

function create_modal(id, backdrop='static'){
    container = document.createElement('div')
    const modalHtml = `
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="${id}" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <img src="../src/img/4quattro/fav4quattro.png" class="imgtoast">
                    <strong class="me-auto">Dados Enviados!</strong>
                    <small>0 min atrás</small>
                    <button type="button" class="btn-close" onclick="location.reload()"></button>
                </div>
                <div class="toast-body">
                    <p>Olá, Seu contato está sendo enviado! Aguarde que nosso corretor responsavel irá entrar em contato</p>
                </div>
            </div>
        </div>
    `;
    container.innerHTML = modalHtml
    document.body.appendChild(container)
    return new bootstrap.Modal(document.getElementById(id), {'show':true, 'backdrop': backdrop})
}

document.getElementById('form').addEventListener('submit', async function (e){
    e.preventDefault()

    nome = document.getElementById('nome').value
    tel = document.getElementById('tel').value
    btn = document.getElementById('btnEmail')


    if(btn && nome && tel){
        const html = `
            <h1>Você tem um novo pedido!</h1>
            <p>Entre em contato para mais detalhes!</p>
            <hr>
            <br>
            <p><strong>Nome: </strong>${nome}</p>
            <p><strong>Telefone: </strong>${tel}</p>
            <a style="background: #5E8B60; color: #fff; padding: 8px; border-radius: 8px; width: 100%;" href="https://wa.me/${tel}">Enviar mensagem no WhatsApp!</a>
            <br>
            <br>
            <hr>
            <a style="color: #5E8B60; text-decoration: none;" href="https://tecnobreve.onrender.com">© Desenvolvido por Tecnobreve, 2025</a>
        `
    
        btn.innerHTML = spinner
        const req = await fetch(
            `https://api.hubbix.com.br/send_mail/${email}`, 
            {
                method: 'POST', 
                headers: {"Content-Type": "application/json"}, 
                body: JSON.stringify({
                    "title": `Novo pedido de Visita - ${nome}`,
                    "html": html
                })
            }
        )
        const res = await req.json()
        modal = create_modal('mdoal', true)
        modal.show()
        if(req.ok){btn.innerHTML = res}
    }else{alert('Dados não informados corretamente!')}
})