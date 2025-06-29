import { createDropdown } from './algolia_dropdown.js';

const searchClient = algoliasearch(algoliaAppId, algoliaApi);

const search = instantsearch({
    indexName: 'movie_index',
    searchClient,
    routing: true,
    insights: true,
});

const MOBILE_WIDTH = 375;

const genreDropdown = createDropdown(instantsearch.widgets.refinementList, {
    closeOnChange: () => window.innerWidth >= MOBILE_WIDTH,
    cssClasses: { root: 'genreDropdown' },
});
const ratingDropdown = createDropdown(instantsearch.widgets.refinementList, {
    closeOnChange: () => window.innerWidth >= MOBILE_WIDTH,
    cssClasses: { root: 'ratingsDropdown' },
});
const languageDropdown = createDropdown(instantsearch.widgets.refinementList, {
    closeOnChange: () => window.innerWidth >= MOBILE_WIDTH,
    cssClasses: { root: 'languageDropdown' },
});

// Render function
const renderHits = (renderOptions, isFirstRender) => {
    const { hits, widgetParams } = renderOptions;

    widgetParams.container.innerHTML = `
        <div class="row mb-4 rounded justify-content-center">
            ${hits
            .map(item =>
                `
                        <div class="col-5 col-md-3 col-lg-2 rounded poster-bg p-2 m-2">
                            <a href="${item.url}">
                                <figure class="mb-0">
                                    <picture>
                                        <img class="img-fluid mb-1 rounded border border-white border-2" src=${item.poster}>
                                    </picture>
                                </figure>
                            </a>
                            <p class="lh-1 mb-1">${item.title}</p>
                            <p class="lh-1 mb-0"><small><span class="badge text-bg-warning rounded-0">Rating: ${item.rating}/10</span></small></p>
                        </div>
                    `
            )
            .join('')}
        </div>
    `;
};

const { connectHits } = instantsearch.connectors;
// Custom widget
const customHits = connectHits(renderHits);

search.addWidgets([
    instantsearch.widgets.stats({
        container: '#stats',
    }),
    instantsearch.widgets.currentRefinements({
        container: '#current-refinements',
        cssClasses: {
            root: 'MyCustomCurrentRefinements float-end',
            item: [
                'bg-dark',
            ],
        }
    }),
    instantsearch.widgets.searchBox({
        container: '#searchbox',
        placeholder: 'Movie title or cast member',
    }),
    customHits({
        container: document.querySelector('#hits'),
    }),
    genreDropdown({
        container: '#genre',
        attribute: 'genre',
    }),
    ratingDropdown({
        container: '#rating',
        attribute: 'rating',
    }),
    languageDropdown({
        container: '#language',
        attribute: 'language',
    }),
    instantsearch.widgets.pagination({
        container: '#pagination',
    }),
]);

search.start();
