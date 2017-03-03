results = run_sql

describe "tests" do
  describe "should contain keywords" do
    it "should contain CREATE" do
      expect($sql.upcase).to include("CREATE")
    end
    
    it "should contain FUNCTION" do
      expect($sql.upcase).to include("FUNCTION")
    end
    
    it "should contain increment" do
      expect($sql.upcase).to include("INCREMENT")
    end
    
    it "should not query people table" do
      expect($sql.upcase).not_to include("PEOPLE")
    end
  end
end