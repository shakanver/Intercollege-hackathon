Vue.component('nice_input', {
    props: ['field_name', 'place_holder',],
    template: '<div class="input-group mb-3"> \
    <div class="input-group-prepend"> \
        <span class="input-group-text" id="basic-addon1">{{field_name}}</span> \
    </div> \
    <input class="form-control" :name="field_name" :placeholder="place_holder" required> \
</div>'
})

vm = new Vue ({
    el: "#vue_app",
    data: {
        courses: ["Maths", "COMP"]
    }
})