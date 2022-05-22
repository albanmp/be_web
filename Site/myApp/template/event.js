function requestPOST(route, param, callb)
{
    fetch(route, {
        method: 'POST',
headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' },
        body: new URLSearchParams(param)
    })
    .then((res) => res.json())
    .then((data) => { callb(data) })
    .catch((err) => console.log(err))
}

const route='/route'
const param={'num': 4,'ecole': 'enac'}
let callb = function(data){
    console.log('Succès de la requête', data)
 }
requestPOST(route, param, callb)