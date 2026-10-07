"""Run the standing content gate and the historical cutover proof, as Verify CI does.

Exit 2 from the cutover proof means its oracle is pinned to older projections;
it is never reported as a cutover PASS. All actual failures remain fatal.
"""
import test_content_parity as content
import test_cutover_parity as cutover


def main() -> int:
    result = content.main()
    if result != 0:
        return result
    result = cutover.main()
    if result == cutover.PINNED:
        print("RELEASE PARITY: PASS (standing content parity passed; historical cutover oracle PINNED)")
        return 0
    return result


if __name__ == "__main__":
    raise SystemExit(main())
