results = run_sql

describe :results do
  it "should return 20 items" do
    expect(results.count).to eq 20
  end
  
  it "should contain only 3 columns" do
    expect(results.first.keys.count).to eq 3
  end
  
  it "should not contain custard column" do
    expect(results.first.keys).not_to include(:custard)
  end
end