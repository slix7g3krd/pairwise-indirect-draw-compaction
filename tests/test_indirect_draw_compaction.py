import pytest
import graphics.indirect_draw_compaction as mod

CASES = [
    ("frame_pair", (1,)),
    ("append_fence", (1,)),
    ("swap_buffer", (1,)),
    ("sort_key", (1,)),
    ("skip_zero", (1,)),
    ("ring_readback", (1,)),
    ("determinism", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("command_build", (1,)),
    ("metrics", (1,)),
    ("instance_count", (1,)),
    ("indirect_args", (1,)),
    ("submit", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
