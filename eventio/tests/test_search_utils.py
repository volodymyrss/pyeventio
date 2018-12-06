from pkg_resources import resource_filename


test_file = resource_filename('eventio', 'resources/gamma_test.simtel.gz')


def test_find_all_subobjects():
    from eventio import EventIOFile
    from eventio.search_utils import find_all_subobjects
    from eventio.simtel import ArrayEvent, TelescopeEvent, ADCSamples

    with EventIOFile(test_file) as f:
        adcsamps = find_all_subobjects(
            f, [ArrayEvent, TelescopeEvent, ADCSamples]
        )

        assert len(adcsamps) == 50
