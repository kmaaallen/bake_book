//Helper functions 
function clickFirstAddBtn(){
    document.getElementsByClassName('add-btn')[0].click();
}

function clickFirstTextAreaAddBtn(){
    document.getElementsByClassName('textarea-add-btn')[0].click();
}

function clickFirstDelBtnIng(){
    document.getElementsByClassName('del-btn-ing')[0].click();
}

function clickFirstDelBtnStep(){
    document.getElementsByClassName('del-btn-step')[0].click();
}

//mock onReady function with if conditions reversed as both submit-preview and edit-preview elements are present index.html
function onReadyReversed() {
    // if recipe_url field is present call showPreview
    if (document.getElementById('submit-preview')) {
        showSubmitPreview();
        document.getElementById('recipe_url').addEventListener('change', showSubmitPreview);
    }
    else if (document.getElementById('edit-preview')) {
        showEditPreview();
        document.getElementById('recipe_url').addEventListener('change', showEditPreview);
    }
}

// function for changing content of recipe_url
function changeRecipeUrl(){
    document.getElementById('recipe_url').value = "";
    document.getElementById('recipe_url').value = "testing";
}


describe("should call add input functions when plus btn clicked", function() {
    it("should call addIngredient function", function() {
        spyOn(window, 'addIngredient');
        clickFirstAddBtn();
        expect(window.addIngredient).toHaveBeenCalled();
    });
    it("should call addStep function", function(){
        spyOn(window, 'addStep');
        clickFirstTextAreaAddBtn();
        expect(window.addStep).toHaveBeenCalled();
    });
});

describe("should call removeInput function when delete button clicked", function(){
    it("should call removeInput function when delete btn in extra ingredient input clicked", function(){
        window.addIngredient();
        spyOn(window, 'removeInput');
        clickFirstDelBtnIng();
        expect(window.removeInput).toHaveBeenCalled();
    });
    it("should call removeInput function when delete btn in extra step input clicked", function(){
        window.addStep();
        spyOn(window, 'removeInput');
        clickFirstDelBtnStep();
        expect(window.removeInput).toHaveBeenCalled();
    });
});

describe("should remove input when removeInput function is clicked", function(){
    beforeEach(function(){
        ing = document.getElementsByClassName('extra-ing-input');
        ingATag = document.getElementsByClassName('add-btn')[0];
        step = document.getElementsByClassName('extra-step-input');
        stepATag = document.getElementsByClassName('textarea-add-btn')[0];
    });
    it("should remove extra ingredient input when that delete btn is clicked", function(){
        window.removeInput(ingATag);
        expect(ing[0]).toBe(undefined);
    });
    it("should remove extra step input when that delete btn is clicked", function(){
        window.removeInput(stepATag);
        expect(step[0]).toBe(undefined);
    });
});


describe("should call show preview functions if preview fields present", function() {
    it("should call showEditPreview if edit-preview element is present", function() {
        spyOn(window, 'showEditPreview');
        onReady();
        expect(window.showEditPreview).toHaveBeenCalled();
    });
    it("should call showSubmitPreview if submit-preview element is present", function() {
        spyOn(window, 'showSubmitPreview');
        onReadyReversed();
        expect(window.showSubmitPreview).toHaveBeenCalled();
    });
});

describe("should call show preview functions when recipe_url field changes", function(){
    beforeEach(function(){
        window.document.getElementById('recipe_url').value = "test";
    });
    it("should call showEditPreview if recipe_url changes", function(){
        spyOn(window, 'showEditPreview');
        window.document.getElementById('recipe_url').value = "testing";
        expect(window.showEditPreview).toHaveBeenCalled();
    });
});

