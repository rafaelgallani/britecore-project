<template>
  <div class="new-risk-type">
    <FormulateForm name="main" class="form-content" v-model="form" @submit="save" >
      <header class="header">
        <h2 class="title">
          New Risk
        </h2>
        <FormulateInput type="submit">Save</FormulateInput>
      </header>
      <div class="form-details">
        <FormulateInput type="text" label="Name" name="name" validation="required" />
        <FormulateInput type="text" label="Description" name="description"
          validation="required" />
      </div>
      <div class="form-fields">
        <FormulateInput class="form-fields-group" type="group" name="fields" label="Default fields"
          help="These fields will be added by default when you create a new risk of this type."
          add-label="Add Field" validation="required" :repeatable="true"  #default="{ index }" :remove="true" minimum="1"
        >
          <a v-if="isFieldTypeEnum(index)"/>
          <div class="field" >
            <FormulateInput name="field_type" type="select" label="Type" validation="required" :options="Constants.FIELD_TYPES" />
            <FormulateInput name="name" label="Name" type="text" validation="required" />
            <div class="line-break"></div>
            <FormulateInput v-if="isFieldTypeEnum(index)" class="field-options" type="group" name="options" label="Values"
              minimum="1" add-label="Add Field" validation="required" :repeatable="true">
              <div class="field">
                <FormulateInput name="label" label="Label" type="text" validation="required" />
                <FormulateInput name="value" label="Value" type="text" validation="required" />
              </div>
            </FormulateInput>
          </div>
        </FormulateInput>
      </div>
    </FormulateForm>
  </div>
</template>

<script>
  import Vue from "vue";
  import * as VueFormulate from "@braid/vue-formulate";
  import axios from "axios";
  Vue.use(VueFormulate.default);
  export default {
    name: "NewRiskType",
    title: "Create - Risk Type",
    data: function () {
      return {
        Constants: {
          FIELD_TYPES: { 
            TEXT: "Text", 
            NUMBER: "Number", 
            DATE: "Date", 
            ENUM: "Options"
          },
        },
        loading: false,
        loader: null,
        form: {
          name: "",
          description: "",
          fields: [],
        }
      };
    },
    methods: {

      toggleLoading(toggle){
        this.loading = toggle;
        if (toggle) this.loader = this.$loading.show();
        if (!toggle) if (this.loader) this.loader.hide();
      },
      
      isFieldTypeEnum(index){
        return this.form.fields[index] && this.form.fields[index].field_type === "ENUM";
      },

      async save(){
        this.toggleLoading(true);
        try {
          const result = await axios.post("/api/v1/risk-type/", this.form);
          
          this.$toastr.s(`Risk type "${result.data.name}" created successfully.`);
          this.reset();
          
        } catch (e){
          this.$toastr.e(`An error occurred when trying to create the risk: ${e}`);
        }
        this.toggleLoading(false);
      },

      reset(){
        this.$formulate.reset("main", {
          name: "",
          description: "",
          fields: [{
            field_type: "TEXT"
          }],
        });

        this.$forceUpdate();
      }
    }
  };

</script>

<style lang="scss">
  @import "@/../node_modules/@braid/vue-formulate/themes/snow/snow.scss";
  @import "@/assets/style/vue-formulate-override.scss";
  @import "@/assets/style/form-reset.scss";
</style>
