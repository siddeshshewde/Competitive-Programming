# calling run_sql will print the results and return them so that you can test data within them.
# if you want to test different sets of data, then its best to move this code into its own top level describe
# block. If you are only testing one set though, its better to set the results before you enter a describe block
# so that the results are presented at the top of the output.
results = run_sql

describe :items do
   it "should return 1 item" do
    expect(results.count).to eq 1
   end
end

describe :columns do
    it "should return 1 columns" do
      expect(results.first.keys.count).to eq 1
    end
end