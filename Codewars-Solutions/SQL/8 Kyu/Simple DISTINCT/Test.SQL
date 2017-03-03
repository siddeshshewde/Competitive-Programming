results = run_sql

describe :query do
  describe "should contain keywords" do
    it "should contain DISTINCT" do
      expect($sql.upcase).to include("DISTINCT")
    end
    
    it "should contain not GROUP BY" do
      expect($sql.upcase).not_to include("GROUP BY")
    end
  end

  describe :columns do
    it "should return 1 columns" do
      expect(results.first.keys.count).to eq 1
    end
    
    it "should return a age column" do
      expect(results.first.keys).to include(:age)
    end
  end
  
  describe :rows do
    it "should return all unique ages" do
     ages = []
     results.each do |result|
       expect(ages).to satisfy { |value| value != result[:age] }
       ages.push(result[:age])
     end
   end
  end
end