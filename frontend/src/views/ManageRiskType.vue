<template>
  <div class="manage-risk-type">
    <div v-for="form in risks" :key="form.id">
      <FormulateForm name="main" class="form-content" >
        <header class="header">
          <h2 class="title">
            {{form.name}}
          </h2>
          <FormulateInput type="submit" @click="listCreatedRisks(form)">View risks</FormulateInput>
        </header>
        <div class="form-details">
          <FormulateInput type="text" label="Name" name="name" :value="form.name" validation="required" disabled="true" />
          <FormulateInput type="text" label="Description" name="description" :value="form.description" validation="required" disabled="true" />
        </div>
        <div class="form-fields">
          <FormulateInput class="form-fields-group" type="group" v-model="form.fields" label="Default fields"
            help="These fields will be added by default when you create a new risk of this type."
            validation="required" :repeatable="true"  #default="{ index }" :minimum="form.fields.length"
          >
            <a v-if="isFieldTypeEnum(index, form.fields)"/>
            <div class="field" >
              <FormulateInput name="field_type" type="select" label="Type" validation="required" :options="Constants.FIELD_TYPES" disabled="true"/>
              <FormulateInput name="name" label="Name" type="text" validation="required" disabled="true"/>
              <FormulateInput name="required" label="Required?" type="checkbox" disabled="true"/>

              <FormulateInput v-if="isFieldTypeEnum(index, form.fields)" class="field-options" type="group" name="options" label="Values"
                minimum="1" add-label="Add Field" validation="required" :repeatable="true">
                <div class="field">
                  <FormulateInput name="label" label="Label" type="text" validation="required" disabled="true"/>
                  <FormulateInput name="value" label="Value" type="text" validation="required" disabled="true"/>
                </div>
              </FormulateInput>
            </div>
          </FormulateInput>
        </div>
      </FormulateForm>
    </div>
  </div>
</template>

<script>
  import Vue from "vue";
  import * as VueFormulate from "@braid/vue-formulate";
  import axios from "axios";
  Vue.use(VueFormulate.default);
  export default {
    name: "ManageRiskType",
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
        risks: [],
      };
    },
    
    async mounted() {
      try {
        const riskTypesResponse = await axios.get("/api/v1/risk-type/");
        this.risks = riskTypesResponse.data;
      } catch (e){
        this.$toastr.e(`An error occurred when trying to retrieve the risk types: ${e}`);
      }
    },

    methods: {
      isFieldTypeEnum(index, fields){
        if (index >= 0 && fields){
          return fields[index] && fields[index].field_type === "ENUM";
        }
        return false;
      },

      async listCreatedRisks(form){
        this.$router.push("/manage/risktype/" + form.id);
      },
    }
  };

</script>

<style lang="scss">
  @import "@/../node_modules/@braid/vue-formulate/themes/snow/snow.scss";
  @import "@/assets/style/vue-formulate-override.scss";

  .title {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .header {
    width: 100%;
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

    .formulate-input-group-add-more{
      display: none;
    }
    
    .formulate-input-group-repeatable {
        border-bottom: none!important;
    }
  }

</style>
