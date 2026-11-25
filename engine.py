def evaluate(data, fixture_path):
    rules = data["rules"]
    findings = []
    for index, decision in enumerate(data["decisions"]):
        if type(decision["executed"]) is not bool or type(decision["approved"]) is not bool:
            raise ValueError("execution and approval must be booleans")
        rule = rules.get(decision["tool"])
        allowed = (
            rule is not None
            and decision["principal"] in rule["principals"]
            and (rule["approval"] is False or decision["approved"] is True)
        )
        if decision["executed"] and not allowed:
            findings.append({"code": "execution_outside_policy", "decision": index})
    return findings
