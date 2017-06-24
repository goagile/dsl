(function() {

    // context variables
    var currentComputer = null,
        currentDisc = null;


    function computer() {
        currentComputer = {
            processor: {},
            discs: []
        };
    }

    function processor() {}

    function cores(value) {
        currentComputer.processor.cores = value;
    }

    function speed(value) {
        if (!currentDisc) {
            currentComputer.processor.speed = value;
        } else {
            currentDisc.speed = value;
        }
    }

    function i386() {
        currentComputer.processor.type = 'i386';
    }

    function disk() {
        currentDisc = {};
        currentComputer.discs.push(currentDisc);
    }

    function size(value) {
        currentDisc.size = value;
    }

    function sata() {
        currentDisc.serial = 'SATA';
    }

    %s

    return currentComputer;
}())