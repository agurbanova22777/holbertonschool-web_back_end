export default function guardrail(mathFunction){
    const queue = [];
    try {
        queue.push(mathFunction());
    }
    catch(error){
        queue.push(error.message);
    }
    finally{
        queue.push("Guradrail was processed");
    }

    return queue;
}
