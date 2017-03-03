results = run_sql

describe :query do
  describe "should contain keywords" do    
    it "should contain GROUP BY" do
      expect($sql.upcase).to include("GROUP BY")
    end
    
    it "should contain COUNT" do
      expect($sql.upcase).to include("COUNT")
    end
  end

  describe :columns do
    it "should return 2 columns" do
      expect(results.first.keys.count).to eq 2
    end
    
    it "should return a age column" do
      expect(results.first.keys).to include(:age)
    end
    
    it "should return a count column" do
      expect(results.first.keys).to include(:people_count)
    end
  end
end