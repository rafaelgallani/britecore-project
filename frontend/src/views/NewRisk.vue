<template>
  <div class="new-risk">
    <header class="header">
      <h2 class="title">
        New Risk
      </h2>
      <button class="form-button" @click="save">Save</button>
    </header>
    <FormulateForm class="form-content" v-model="risk">
      <div class="form-details">
        <FormulateInput
          name="type"
          :options="riskTypes"
          type="select"
          @input="getTypeFields"
          placeholder="Select a risk type"
          label="Risk Type"
        />
        <FormulateInput type="text" label="Name" name="name" validation="required" />
        <FormulateInput type="text" label="Description" name="description"
          validation="required" />
      </div>
      <div class="form-fields" v-if="risk.type != null">
        <FormulateInput class="form-fields-group" type="group" name="fields" label="Default fields"
          :help="`The fields for the ${getSelectedRiskTypeLabel()} risk type.`"
          validation="required" #default="{ index }" :minimum="risk.fields.length"
        >
          <div v-if="risk.fields[index] != null" class="field" >
            <!-- <FormulateInput name="name" label="Name" type="text" validation="required" /> -->
            <FormulateInput name="value" :label="risk.fields[index].name" :type="getInputType(risk.fields[index])" validation="required" :options="risk.fields[index].options"/>
          </div>
        </FormulateInput>

        <FormulateInput class="form-fields-group" type="group" name="customFields" label="Custom fields"
          help="These fields will only be added to this specific risk. You can use this section to add information present only in this particular record."
          add-label="Add Custom Field" validation="required" :repeatable="true"  #default="{ index }" minimum="0"
        >
          <a v-if="risk.customFields[index] && risk.customFields[index].type === 'enum' "/>
          <div v-if="risk.customFields[index] != null" class="field" >
            <FormulateInput name="type" type="select" label="Type" validation="required" :options="Constants.FIELD_TYPES" />
            <FormulateInput name="name" label="Name" type="text" validation="required" />
            <FormulateInput name="value" label="Value" :type="getInputType(risk.customFields[index])" validation="required" :options="risk.customFields[index].options"/>

            <FormulateInput v-if="risk.customFields[index].type === 'enum'" class="field-options" type="group" name="options" label="Values"
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
  export default {
    name: "NewRisk",
    data: function () {
      return {
        Constants: {
          FIELD_TYPES: { 
            text: "Text", 
            number: "Number", 
            date: "Date", 
            enum: "Option"
          },
        },
        riskTypes: [
          {
            label: "Car",
            value: "car",
          },
          {
            label: "House",
            value: "house",
          },
          {
            label: "Prize",
            value: "prize",
          }
        ],
        risk: {
          name: null,
          type: null,
          description: null,
          fields: [],
          customFields: [],
        }
      };
    },
    methods: {
      save(){
        console.log(this.risk);
      },

      getSelectedRiskTypeLabel(){
        return this.riskTypes.find(riskType => riskType.value === this.risk.type).label;
      },

      getInputType(field){
        if (field.type === "enum") return "select";
        return field.type;
      },
      
      async getTypeFields(typeId){
        const fields = await new Promise((resolve) => {
          resolve([
            {
              name: `Name - ${typeId}`,
              type: "text",
            },
            {
              name: "Test",
              type: "text",
            },
            {
              name: "Created date",
              type: "date",
            },
            {
              name: "Xd",
              type: "enum",
              options: [
                {
                  label: "v1", 
                  value: "Valor 1",
                },
                {
                  label: "v2", 
                  value: "Valor 2",
                },
                {
                  label: "v3", 
                  value: "Valor 3",
                },
              ]
            },
          ]);
        });

        this.risk.fields = fields;
        return fields;
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
