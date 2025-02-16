LLM_RULE_EXTRACTION_PROMPT_TEMPLATE1 = """Use the following step-by-step instructions to respond to user inputs. 
Step 1 - The user will provide you with multiple paragraphs of input text. Each paragraph will be enclosed in triple quotes. 
         Each paragraph starts with the pattern {"id": "digit.(1)", "id":"digit.(1).1, "id":"digit.(1).1a,"id":"digit.(1).2"} 
         where "digit.(1)","digit.(1).1a, and "digit.(1).2" are variables and represents the id's of that paragraph.
         Provide an output for each input paragraph and enclose the output for each paragraph in "###". 
         Extract the first order predicate logic from each paragraph using the python output format provided in the following 
         example: The input paragraph may contain the sentences or words like "considered income from non-independent work","not considered income from non-independent work",
         "taxpayer age","pensions starting","pension benefit","deductible expenses","exemptions","relevant tax rates","deductions are applicable for",
         "specific exemptions or special considerations","Salaries, wages, bonuses and other benefits","allowances"
         If id's are nested then extracet as fallows
         [
           {
  "1": {
    "1.1": {
      "1.1.1": {
        "1.1.1.1": {
          "19.1.1.1a": [
            "19.1.1.1a",
            "AND"
          ]
        },
        "1.1.1.2": [
          "19.1.1.2",
          "AND"
        ],
        "1.1.1.3": [
          "19.1.1.3",
          "AND"
        ],
        "1.1.1": [
            "19.1.1",
            "AND"
        ]
      },
      "1.1.2": [
        "19.1.2",
        "AND"
      ],
      "1.1.3": [
        "19.1.3",
        "AND"
      ],
      "1.1.4": [
        "19.1.4",
        "AND"
      ]
    }
  }
}
        ]
         otherwiase extracet as fallows
         
         So extracted as follows: [{"id": "digit.(1)"}, 
         {"emit": {"field": "Person", "condition": "is", "value": True}}, 
         {"combinator": "AND"}, {"emit": {"field": "pension", "condition": "is", "value": True}}, 
         {"combinator": "AND"}, {"emit": {"field": "salary", condition": " is ", "value": True}}, 
         {"combinator": "AND"}, {"emit": {"field": "age", "condition": ">=", "value": "receive pension benefits"}}].
         Remember to take into account the entire text in the respective input paragraph while extracting the first order predicate logic. 
         Here, field names "field", "condition" and "value" must remain constant but their values change based on the text from which the 
         first order predicate logic is extracted. The "combinator" can have values "AND" or "OR" representing the logical AND or OR 
         operations between the different instances of "emit". The "condition" can have the values "is", "<", ">", "<=" or ">=". 
         If boolean, the value of "value" can be True or False, not true or false. If not boolean, its value can be anything like a 
         number or text. Split the values of "field" to their smallest possible values. As an example, 
         split "is_regular_student_at_6th_grade_in_granite_oaks_school" into "regular_student", "6th_grade" and "granite_oaks_school". 
         For similar input paragraph text, use the same values for "field" as used in the extracted first order predicate logic for 
         previous paragraphs in this run of the prompt. If you cannot extract the output for a given input paragraph, please provide the 
         output for that paragraph as in the following example: [{"id": digit.(1)}], where digit.(1)" is the "id" of that input paragraph. 
Step 2 - Add "emit" to all the nodes if not added already as shown in the example. 
Step 3 - Enclose the combinator in {}. As an example, {"combinator": "AND"}. if not done already. 
Step 4 - Remove the english sentences, and extra plain text or characters such as `, ", python, etc., other than ###, at the beginning or end of your output. 
Step 5 - Remove newline characters and tab characters from your response. 
Step 6 - Enclose the output of each paragraph using [] if not already done so. 
Step 7 - Enclose the output of each input paragraph in ### both at the beginning and end. 
Step 8 - Ensure that all the opening brackets such as { and [ have a corresponding closing bracket } and ] respectively in their correct places.
"""

ruleset = {'19.1.1': [('19.1.1', 'LLM', '19.1.1', 'is', 'energy_price_allowance', True), ('19.1.1', 'LLM', '19.1.1', 'is', 'income', True), ('19.1.1', 'LLM', '19.1.1', 'is', 'pension_benefit', True), ('19.1.1', 'LLM', '19.1.1', 'is', 'wage_tax_deduction', False)], '19.1.1.1': [('19.1.1.1', 'LLM', '19.1.1.1', 'is', 'energy_price_allowance', True), ('19.1.1.1', 'LLM', '19.1.1.1', 'is', 'income', True), ('19.1.1.1', 'LLM', '19.1.1.1', 'is', 'pension_benefit', True), ('19.1.1.1', 'LLM', '19.1.1.1', 'is', 'wage_tax_deduction', False), ('19.1.1.1', 'LLM', '19.1.1.1', 'is', 'pension', True), ('19.1.1.1', 'LLM', '19.1.1.1', 'is', 'civil_service_law', True)], '19.1.1.1a': [('19.1.1.1a', 'LLM', '19.1.1.1a', 'is', 'energy_price_allowance', True), ('19.1.1.1a', 'LLM', '19.1.1.1a', 'is', 'income', True), ('19.1.1.1a', 'LLM', '19.1.1.1a', 'is', 'pension_benefit', True), ('19.1.1.1a', 'LLM', '19.1.1.1a', 'is', 'wage_tax_deduction', False), ('19.1.1.1a', 'LLM', '19.1.1.1a', 'is', 'company_event', True), ('19.1.1.1a', 'LLM', '19.1.1.1a', 'is', 'income_from_non_self_employed_work', False)], '19.1.1.2': [('19.1.1.2', 'LLM', '19.1.1.2', 'is', 'energy_price_allowance', True), ('19.1.1.2', 'LLM', '19.1.1.2', 'is', 'income', True), ('19.1.1.2', 'LLM', '19.1.1.2', 'is', 'pension_benefit', True), ('19.1.1.2', 'LLM', '19.1.1.2', 'is', 'wage_tax_deduction', False), ('19.1.1.2', 'LLM', '19.1.1.2', '>=', 'age_limit', '63'), ('19.1.1.2', 'LLM', '19.1.1.2', '>=', 'severely_disabled', '60')], '19.1.1.3': [('19.1.1.3', 'LLM', '19.1.1.3', 'is', 'energy_price_allowance', True), ('19.1.1.3', 'LLM', '19.1.1.3', 'is', 'income', True), ('19.1.1.3', 'LLM', '19.1.1.3', 'is', 'pension_benefit', True), ('19.1.1.3', 'LLM', '19.1.1.3', 'is', 'wage_tax_deduction', False), ('19.1.1.3', 'LLM', '19.1.1.3', 'is', 'employer_contributions', True), ('19.1.1.3', 'LLM', '19.1.1.3', 'is', 'special_payments', False)], '19.1.2': [('19.1.2', 'LLM', '19.1.2', 'is', 'benefits', True)], '19.1.3': [('19.1.3', 'LLM', '19.1.3', 'is', 'pension_allowance', True), ('19.1.3', 'LLM', '19.1.3', 'is', 'pension_benefit', True), ('19.1.3', 'LLM', '19.1.3', 'is', 'maximum_amount', True), ('19.1.3', 'LLM', '19.1.3', 'is', 'supplement', True)], '19.1.4': [('19.1.4', 'LLM', '19.1.4', 'is', 'pension_allowance', True), ('19.1.4', 'LLM', '19.1.4', 'is', 'pension_benefit', True), ('19.1.4', 'LLM', '19.1.4', 'is', 'special_payments', True), ('19.1.4', 'LLM', '19.1.4', 'is', 'legal_claim', True), ('19.1.4', 'LLM', '19.1.4', 'is', 'supplement', True)]}
ruleset_list = [('19.1.1', 'AND'), ('19.1.1.1', 'AND'), ('19.1.1.1a', 'AND'), ('19.1.1.2', 'AND'), ('19.1.1.3', 'AND'), ('19.1.2', 'AND'), ('19.1.3', 'AND'), ('19.1.4', 'AND')]
