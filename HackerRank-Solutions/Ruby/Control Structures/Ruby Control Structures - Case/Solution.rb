def identify_class(obj)
    # write your case control structure here
    objectDesc = case obj
        when Hacker then "It's a Hacker!"
        when Submission then "It's a Submission!"
        when TestCase then "It's a TestCase!"
        when Contest then "It's a Contest!"
        else "It's an unknown model"
    end
        
   puts objectDesc
        
end