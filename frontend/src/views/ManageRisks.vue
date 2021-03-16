<template>
  <div class="manage-risk">
    <div v-for="risk in risks" :key="risk.id">
      <FormulateForm name="main" class="form-content" >
        <header class="header">
          <h2 class="title">
            {{risk.name}}
          </h2>
        </header>
        <div class="form-details">
          <FormulateInput type="text" label="Name" name="name" :value="risk.name" validation="required" disabled="true" />
          <FormulateInput type="text" label="Description" name="description" :value="risk.description" validation="required" disabled="true" />
        </div>
        <div class="form-fields">
          <FormulateInput class="form-fields-group" type="group" v-model="risk.fields" :label="`${risk.name} fields`"
            validation="required" :repeatable="true"  #default="{ index }" :minimum="risk.fields.length"
          >
            <a v-if="isFieldTypeEnum(index, risk.fields)"/>
            <div v-if="risk.fields[index]" class="field" >
              <FormulateInput :value="risk.fields[index].field.field_type" type="select" label="Type" validation="required" :options="Constants.FIELD_TYPES" disabled="true"/>
              <FormulateInput :value="risk.fields[index].field.name" label="Name" type="text" validation="required" disabled="true"/>
              <FormulateInput name="value" label="Value" :type="getInputType(risk.fields[index].field)" validation="required" :options=" risk.fields[index].field.options" disabled="true" :value="risk.fields[index].value"/>

              <FormulateInput v-if="isFieldTypeEnum(index, risk.fields)" class="field-options" type="group" v-model="risk.fields[index].field.options" label="Values"
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
    <div v-if="risks.length === 0 && !loading">
      <div class="error-message">
        No risks found for "{{this.risk.name}}" risk.
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from "vue";
  import * as VueFormulate from "@braid/vue-formulate";
  import axios from "axios";
  Vue.use(VueFormulate.default);
  export default {
    name: "ManageRisks",
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
            "TEXT": "text",
            "NUMBER": "number",
            "DATE": "date",
          },
        },
        loading: true,
        loader: null,
        riskType: {},
        risks: [],
      };
    },
    
    async mounted() {
      this.toggleLoading(true);
      try {
        const { riskTypeId } = this.$route.params;
        const riskTypesResponse = await axios.get(`/api/v1/risk-type/${riskTypeId}`);
        this.risk = riskTypesResponse.data;
        this.risks = this.risk;
      } catch (e){
        this.$toastr.e(`An error occurred when trying to retrieve the risks: ${e}`);
      }
      this.toggleLoading(false);
    },

    methods: {

      toggleLoading(toggle){
        this.loading = toggle;
        if (toggle) this.loader = this.$loading.show();
        if (!toggle) if (this.loader) this.loader.hide();
      },
      
      isFieldTypeEnum(index, fields){
        if (index >= 0 && fields){
          return fields[index] && fields[index].field_type === "ENUM";
        }
        return false;
      },

      getInputType(field){
        if (field.field_type === "ENUM") return "select";
        return this.Constants.htmlFieldTypeMap[field.field_type];
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
  }

  .manage-risk .formulate-input-group-add-more{
    display: none!important;
  }
  
  .manage-risk .formulate-input-group-repeatable {
      border-bottom: none!important;
  }

</style>
