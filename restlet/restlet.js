/**
 * @NApiVersion 2.x
 * @NScriptType Restlet
*/
define(['N/search'], function(search) {

    function getAllResults(){

        var mySearch = search.load({
            id: 'reportName or customName'
        });

        var results=mySearch.run();
        var searchResults=[];
        var searchId=0;
        do{
            var resultRange=results.getRange({
                    start:searchId,
                    end:searchId+1000

            });
            resultRange.forEach(function(slice){
                searchResults.push(slice);
                searchId++;

            });
        }while (resultRange.length>=1000);
        return JSON.stringify(searchResults);
    }
    return{
        get: getAllResults
    }
    
});  
