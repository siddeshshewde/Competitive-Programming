results = run_sql

describe :items do
   it "should return 10 items" do
    expect(results.count).to eq 10
   end

   it "should return isbn numbers" do
     results.each do |result|
       expect(result[:isbn]).to be_a String
     end
   end
   
   it "should return names" do
     results.each do |result|
       expect(result[:name]).to eq find_record(:products, result[:id]).name
     end
   end
   
   it "should return company names" do
    results.each do |result|
      company = find_record(:companies, result[:company_id])
      expect(result[:company_name]).to eq company.name
    end
   end
end