const url_users = "http://127.0.0.1:8004/users/users/"

const div = document.getElementById("div")


async function getUsers() {
    const res = await fetch(url_users)
    if(!res.ok){
        throw new Error(`There's some problem happened${res.status}`);        
    }
    const data = await res.json()
    console.log(data)
    div.innerHTML = data
    return data;
}

(async () => {
    const result = await getUsers()
    return result;
})
