const pensador = require('pensador-api')

var author = 'Albert EinsteinAlbert Einstein'
async function phrase(){
    const array = await pensador({ term: "Albert EinsteinAlbert Einstein", max: 1 })
    console.log(array)
}


phrase()