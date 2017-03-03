results = run_sql

describe :items do
   it "should return people with age over 50" do
     record_count = get_all_records(:people).count
     expect(results.count).to eq record_count
   end
   
   it "should return names" do
     results.each do |result|
       expect(result[:name]).to eq find_record(:people, result[:id]).name
     end
   end
   
   it "should only return people with age over 50" do
     results.each do |result|
       expect(result[:age]).to be > 50
     end
   end
   
   it "should only return people ordered by age decending" do
     last_highest = 100
     results.each do |result|
       expect(result[:age]).to be <= last_highest
       last_highest = result[:age]
     end
   end
end