import {uploadPhoto, createUser} from "./utils.js"

export default function handleProfileSignup(){
    return Promise.all([
        uploadPhoto(),
        createUser()
    ])
    .then((results) => {
        console.log(`${results.body} ${results.firstName} ${results.lastName}`);
    })
    .catch(() => {
        console.log("Signup system offline");
    })
}
