from benchmarks.run_sample import run_sample
from mentat import Mentat
from mentat.conversation import MentatAssistantMessageParam
from mentat.parsers.parser import ParsedLLMResponse
    mock_session_context.config.sampler = True
            MentatAssistantMessageParam(
                parsed_llm_response=ParsedLLMResponse("", "test_assistant_content", []),
    sampler.set_active_diff()
    assert remove_checksums(sample.diff_active) == remove_checksums(expected_diff)
    assert sample.message_history == []
    assert sample.message_prompt == "test_user_content"
    assert sample.message_edit == "test_assistant_content"
    assert sample.context == ["multifile_calculator/operations.py"]
    assert sample.diff_edit == ""
    assert sample.version == "0.2.0"
    parsedLLMResponse = GitParser().parse_llm_response(test_sample["diff_edit"])
    result = await run_sample(sample)
    diff_eval = result["diff_eval"]
    sample.version = "2.3"
    parsedLLMResponse = GitParser().parse_llm_response(diff_edit)
    client = Mentat(cwd=temp_testbed, paths=["."])
    await client.startup()
    client.session.ctx.config.sampler = True
    await client.call_mentat_auto_accept(dedent("""\
    client.session.ctx.code_context.include_files = {}
    await client.call_mentat(f"/sample {temp_testbed.as_posix()}")
    await client.call_mentat(merge_base)
    await client.call_mentat("test_url")
    await client.call_mentat("test_title")
    await client.call_mentat("test_description")
    await client.call_mentat("test_test_command")
    await client.call_mentat("q")
    await client.shutdown()
    assert sample.message_edit == "I will make the following edits."
    result = await run_sample(sample, temp_testbed)
    diff_eval = result["diff_eval"]