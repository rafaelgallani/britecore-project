<template>
  <div class="new-risk">
    <FormulateForm name="risk-form" class="form-content" v-model="risk" @submit="save">
      <header class="header">
        <h2 class="title">
          New Risk
        </h2>
        <FormulateInput type="submit">Save</FormulateInput>
      </header>
      <div class="form-details">
        <FormulateInput
          name="risk_type"
          :options="riskTypes"
          type="select"
          @input="getTypeFields"
          placeholder="Select a risk type"
          label="Risk Type"
          validation="required"
        />
        <FormulateInput type="text" label="Name" name="name" validation="required" />
        <FormulateInput type="text" label="Description" name="description"
          validation="required" />
      </div>
      <div class="form-fields" v-if="risk.risk_type != null">
        <FormulateInput class="form-fields-group" type="group" name="fields" label="Default fields"
          :help="`The fields for the ${getSelectedRiskTypeLabel()} risk type.`"
          validation="required" #default="{ index }" :minimum="risk.fields.length"
        >
          <div v-if="risk.fields[index] != null" class="field" >
            <FormulateInput name="value" :label="risk.fields[index].name" :type="getInputType(risk.fields[index])" validation="required" :options="risk.fields[index].options"/>
          </div>
        </FormulateInput>

        <FormulateInput class="form-fields-group" type="group" name="customFields" label="Custom fields"
          help="These fields will only be added to this specific risk. You can use this section to add information present only in this particular record."
          add-label="Add Custom Field" :repeatable="true"  #default="{ index }" minimum="0"
        >
          <a v-if="risk.customFields[index] && risk.customFields[index].field_type === 'ENUM' "/>
          <div v-if="risk.customFields[index] != null" class="field" >
            <FormulateInput name="field_type" type="select" label="Type" validation="required" :options="Constants.FIELD_TYPES" />
            <FormulateInput name="name" label="Name" type="text" validation="required" />
            <FormulateInput name="value" label="Value" :type="getInputType(risk.customFields[index])" validation="required" :options="risk.customFields[index].options"/>

            <FormulateInput v-if="risk.customFields[index].field_type === 'ENUM'" class="field-options" type="group" name="options" label="Values"
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
  Vue.use(VueFormulate.default);
  import axios from "axios";
  export default {
    name: "NewRisk",
    data: function () {
      return {
        Constants: {
          FIELD_TYPES: { 
            TEXT: "Text", 
            NUMBER: "Number", 
            DATE: "Date", 
            ENUM: "Options"
          },
          htmlFieldTypeMap: {
            "Text": "text",
            "Number": "number",
            "Date": "date",
          },
        },
        riskTypes: [],
        risk: {
          name: null,
          risk_type: null,
          description: null,
          fields: [],
          customFields: [],
        }
      };
    },
    
    async mounted() {
      try {
        const riskTypesResponse = await axios.get("http://0.0.0.0:8000/api/v1/risk-type/?fields=id,name");
        this.riskTypes = riskTypesResponse.data.map(a => ({ label: a.name, value: a.id }));
      } catch (e){
        this.$toastr.e(`An error occurred when trying to retrieve the risk types: ${e}`);
      }
    },

    methods: {
      async save(){
        try {
          const result = await axios.post("http://0.0.0.0:8000/api/v1/risk/", this.risk);
          
          this.$toastr.s(`Risk "${result.data.name}" created successfully.`);
          this.reset();
          
        } catch (e){
          this.$toastr.e(`An error occurred when trying to create the risk: ${e}`);
        }
      },

      reset(){
        this.$formulate.reset("risk-form", {
          name: null,
          risk_type: null,
          description: null,
          fields: [],
          customFields: [],
        });
      },

      getSelectedRiskTypeLabel(){
        return this.riskTypes.find(riskType => riskType.value === this.risk.risk_type).label;
      },

      getInputType(field){
        if (field.field_type === "ENUM") return "select";
        return this.Constants.htmlFieldTypeMap[field.field_type];
      },
      
      async getTypeFields(typeId){
        if (!typeId) return;
        try {
          const riskTypesResponse = await axios.get(`http://0.0.0.0:8000/api/v1/risk-type/${typeId}/?fields=fields`);
          this.risk.fields = riskTypesResponse.data.fields;
        } catch (e){
          this.$toastr.e(`An error occurred when trying to retrieve the risk types: ${e}`);
        }
      }
    }
  };

</script>

<style lang="scss">
  @import "@/../node_modules/@braid/vue-formulate/themes/snow/snow.scss";
  //@import "@/assets/style/vue-formulate-override.scss";

  .title {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .header {
    display: flex;
    justify-content: space-between;
    .form-button {
      font-size: 15px;
      padding: 10px 20px;
      color: $text-on-primary;
      background: $primary-color;
      border-radius: 5px;
      cursor: pointer;
    }
  }

  .form-content {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    padding: 10px;
    margin: auto;
    margin-top: 20px;

    .form-fields{
      width: 100%;

      .form-fields-group {
        width: 100%;
      }

      .field .field-options {
        position: relative;
        flex-basis: 85%;
        margin-top: 30px;

        .formulate-input{
          width: calc(50% - 20px);
        }
      }
    }

    &>.form-details{
      flex-basis: 100%;
      display: flex;

      .formulate-input + .formulate-input {
        padding-left: 10em;
      }
    }
  }

</style>
